"""
@title:      雪花算法
@difficulty: 中等
@importance: 5/5
@tags:       业务模拟
@desc:       雪花算法用于生成唯一id，由64位二进制数组成。
             为了避免碰撞，结合了时间戳、分组号、序列号综合生成id，同时兼容了一些碰撞处理。
"""

import time


class Snowflake:
    def __init__(self, data_center_id=0, worker_id=0):
        # 分组id，机器id
        self.data_center_id = data_center_id
        self.worker_id = worker_id
        # 序列id
        self.sequence = 0

        # 上次调用的时间戳
        self.last_timestamp = -1

        # 共64位 首尾符号位固定为 0
        self.timestamp_bits = 41  # 时间戳部分所占的位数
        self.data_center_id_bits = 5  # 数据中心ID所占的位数
        self.worker_id_bits = 5  # 机器ID所占的位数
        self.sequence_bits = 12  # 序列号所占的位数

        # 最大数据中心ID
        self.max_data_center_id = -1 ^ (-1 << self.data_center_id_bits)
        # 最大机器ID
        self.max_worker_id = -1 ^ (-1 << self.worker_id_bits)
        # 最大序列号
        self.max_sequence = -1 ^ (-1 << self.sequence_bits)

        # 确认生成id格式    时间戳 + 数据中心id + 机器码 + 序列号
        # 时间戳左移的位数
        self.timestamp_shift = self.data_center_id_bits + \
            self.worker_id_bits + self.sequence_bits
        # 数据中心ID左移的位数
        self.data_center_id_shift = self.worker_id_bits + self.sequence_bits
        # 机器ID左移的位数
        self.worker_id_shift = self.sequence_bits

    def generate_id(self):
        # 刚好41位
        timestamp = int(time.time() * 1000)

        # 时钟回拨
        if timestamp < self.last_timestamp:
            raise ValueError("时钟倒退，请检查系统时间！")

        # 时间碰撞了
        if timestamp == self.last_timestamp:
            # 序列号
            self.sequence = (self.sequence + 1) & self.max_sequence
            # 序列号用完了 等待时间戳变化
            if self.sequence == 0:
                timestamp = self.wait_next_millis(self.last_timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = timestamp
        # 拼接
        return ((timestamp << self.timestamp_shift) |
                (self.data_center_id << self.data_center_id_shift) |
                (self.worker_id << self.worker_id_shift) |
                self.sequence)

    def wait_next_millis(self, last_timestamp):
        timestamp = int(time.time() * 1000)
        while timestamp <= last_timestamp:
            timestamp = int(time.time() * 1000)
        return timestamp


if __name__ == "__main__":
    snowflake = Snowflake()
    for i in range(10):
        print(snowflake.generate_id())
