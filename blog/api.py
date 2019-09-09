from rest_framework import serializers, generics
from django_filters.rest_framework import FilterSet, DateFilter, DjangoFilterBackend

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    annotation = serializers.SerializerMethodField()
    author_name = serializers.CharField(source='author.name')

    @staticmethod
    def get_annotation(obj: Post):
        return obj.content[:obj.content[100:].find(' ')]

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'annotation', 'author_name', 'created_at')


# class DateIntervalFilter(filters.BaseFilterBackend):
#     def filter_queryset(self, request, queryset, view):
#         date_from = request.query_params.get('date_from')
#         date_to = request.query_params.get('date_to')
#

class DateIntervalFilter(FilterSet):
    date_from = DateFilter(field_name='created_at', lookup_expr='date__gte')
    date_to = DateFilter(field_name='created_at', lookup_expr='date__lte')

    # def filter_queryset(self, queryset):
    #     print(self.form.cleaned_data.items())
    #     return super().filter_queryset(queryset)

    class Meta:
        fields = ('date_from', 'date_to')


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = DateIntervalFilter
