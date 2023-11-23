from django_elasticsearch_dsl import Document, Index, fields
from car.models import Car

car_index = Index("cars")
car_index.settings(
    # should increase shards based on project definition ....
    number_of_shards=1,
    number_of_replicas=0,
)


@car_index.doc_type
class CarDocument(Document):
    owner_full_name = fields.TextField(attr='owner.get_full_name')

    class Django:
        model = Car
        fields = [
            'id',
            'title',
            'description',
            'color',
            'carrying_capacity',
            'cylinder_number',
            'cylinder_capacity'
        ]
