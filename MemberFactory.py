from abc import ABC, abstractmethod
from Member import Member

class MemberFactory(ABC):
    @abstractmethod
    def create_member(self, name, member_id):
        pass

class ConcreteMemberFactory(MemberFactory):
    def create_member(self, name, member_id):
        return Member(name, member_id)
