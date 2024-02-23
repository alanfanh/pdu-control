import serial
import serial.tools.list_ports

def get_comport_list():
    # 获取PC上com串口列表
    port_lists = list(serial.tools.list_ports.comports())
    if len(port_lists) <= 0:
        return False
    else:
        print("可用串口如下：")
        for comport in port_lists:
            print(comport)
        return port_lists

def get_com_num(s):
    # 获取com口号
    string_l = s.split("-")
    return string_l[0]

class Pdu(serial.Serial):
    def __init__(self, port: str , user: str, pwd: str, baudrate: int = 9600, bytesize: int = 8, parity: str = "N", stopbits: float = 1, timeout: float = 1.0, xonxoff: bool = False, rtscts: bool = False, write_timeout: float = None, dsrdtr: bool = False, inter_byte_timeout: float = None) -> None:
        super().__init__(port, baudrate, bytesize, parity, stopbits, timeout, xonxoff, rtscts, write_timeout, dsrdtr, inter_byte_timeout)
        self.user = user
        self.pwd = pwd

    def power_on(self, id) -> None:
        # 断电
        self.send_cmd('olon %d\r' % id)

    def power_off(self, id) -> None:
        # 通电
        self.send_cmd('oloff %d\r' % id)

    def login(self) -> bool:
        # 串口登录PDU
        self.send_cmd('\r\r')
        res = self.read_data(14)
        if ("User Name" in res):
            self.send_cmd(self.user+'\r')
            self.send_cmd(self.pwd+'\r')
            self.send_cmd('\r')
            # print("Login success")
            return True
        else:
            return False

    def is_login(self) -> bool:
        # 判断是否已登录PDU
        self.send_cmd('\r\r\r')
        res = self.read_data(50)
        if ("apc>" in res):
            return True
        else:
            return False

    def logout(self) -> bool:
        try:
            data = self.readlines()
            self.send_cmd('\r\r')
            self.send_cmd('quit\r')
            data = self.read_data(1000)
            # print('---logout:%s ---' % data)
            if ("Bye." in data):
                # print("串口已退出PDU登录")
                return True
        except Exception as e:
            raise('执行命令失败', e)

    def send_cmd(self, cmd: str) -> None:
        # 写入命令
        cmd_bytes = str.encode(cmd)
        self.write(cmd_bytes)
        self.flush()

    def read_data(self, b: int) -> str:
        # 读取指定字节大小的数据,并返回字符串
        data = self.read(b)
        return data.decode("utf-8")

    def closed_comport(self) -> None:
        # 关闭串口
        if self.is_open:
            self.close()

    def get_one_line(self) -> str:
        # 读取串口当行数据，并返回字符串
        data = self.readline()
        return data.decode().strip()

