from abc import ABC, abstractmethod

class AbsractCreateTable(ABC):
    """
        Class of rules, Interface
        Built to create encapsulation
        Inheritance classes must realize all functions
    """

    def __init__(self,table_name):
        """
        :param table_name: str obj tha name of table in SQLServer
        """
        self.table_name = table_name
        super().__init__()

    @abstractmethod
    def create_table(self):
        """
            Abstract method to create table in SQLServer
        """
        pass