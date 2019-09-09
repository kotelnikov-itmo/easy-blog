from rest_framework import serializers, generics
from django_filters.rest_framework import FilterSet, DateFilter, DjangoFilterBackend

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    annotation = serializers.SerializerMethodField()
    author_name = serializers.CharField(source='author.name')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    @staticmethod
    def get_annotation(obj: Post):
        return obj.content if len(obj.content) <= 100 else obj.content[:obj.content.rfind(' ', 0, 101)]

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'annotation', 'author_name', 'created_at')


class DateIntervalFilter(FilterSet):
    date_from = DateFilter(field_name='created_at', lookup_expr='date__gte')
    date_to = DateFilter(field_name='created_at', lookup_expr='date__lte')

    # def filter_queryset(self, queryset):
    #     print(self.form.cleaned_data.items())
    #     return super().filter_queryset(queryset)

    class Meta:
        fields = ('date_from', 'date_to')


class PostListView(generics.ListAPIView):
    """
    Filtering by creation date: date_from, date_to params;
    Use date format %Y-%m-%d (like 2019-11-23)
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = DateIntervalFilter
