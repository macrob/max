from dataclasses import dataclass, field
import uuid


def get_parcel_id() -> str:
  return str(uuid.uuid4())
  
@dataclass(frozen=True)
class Parcel:
  parcel_id: str = field(default='testte')
  # recipient_name: str = field(default_factory=uuid.uuid4)
  recipient_name: str = field(default_factory=get_parcel_id)
  
  @staticmethod
  def get_parcel_id() -> str:
    return str(uuid.uuid4())
  
  def validate(self):
    if self.recipient_name == 'John':
      raise ValueError('John is not allowed')
    pass
  
  def __post_init__(self):
    print(f'post Parcel id: {self.parcel_id}')
    self.validate()
  
  
p1 = Parcel(parcel_id=123, recipient_name='John')
# p.parcel_id = '1234567890'
# p.recipient_name = 'John'
p2 = Parcel()
print(p1)
print(p2)