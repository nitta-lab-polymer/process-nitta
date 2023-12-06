from enum import StrEnum
from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class encodingStr(StrEnum):
    shift_jis = "shift-jis"
    utf_8 = "utf-8"


class CSVConfig(BaseModel):
    encoding: encodingStr = encodingStr.shift_jis
    sep: str = ","
    header: Optional[int] = None
    usecols: Union[List[int], List[str], None] = None
    names: Optional[List[str]] = None
    dtype: Optional[Dict[str, type]] = None
    skiprows: Optional[List[int]] = None  # 冒頭の行を読み飛ばす動作は許可しない
    skipfooter: int = 0
    engine: str = "python"

    def to_dict(self):
        return self.model_dump()

    def Instron(self):
        self.header = 51
        self.skipfooter = 3
        self.usecols = ["Voltage"]
        self.names = ["EndHeader", "日時(μs)", "Voltage"]
        self.dtype = {"Voltage": float}
        return self
