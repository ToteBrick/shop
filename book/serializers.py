from rest_framework import serializers


class BookSerializer1(serializers.Serializer):
    btitle = serializers.CharField()
    bpub_date = serializers.DateField()


class HeroSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    hbook = BookSerializer1()

class BookSerializer(serializers.Serializer):
    btitle = serializers.CharField(min_length=5, max_length=11)
    bpub_date = serializers.DateField(write_only=True)
    bcomment = serializers.IntegerField(min_value=1, max_value=50, default=2)
    # 嵌套序列化返回   PrimaryKeyRelatedField返回关联对象的id值
    # heroinfo_set= serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    # StringRelatedField 返回模型类中 __str__ 方法中返回的数据
    # heroinfo_set= serializers.StringRelatedField(read_only=True,many=True)
    # 根据指定的HeroSerialzier序列化中指定的字段返回
    # heroes = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # heroes = serializers.StringRelatedField(read_only=True, many=True)
    heroes = HeroSerializer(many=True)  # 根据指定的HeroSerialzier序列化中指定的字段返回

    def validated_btitle(self, value):
        if value == 'python':
            raise serializers.ValidationError('书名python错误')
        return value

    def validate(self, attrs):
        pass

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class HeroSerializer1(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
