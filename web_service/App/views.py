from django.http import JsonResponse
import pytesseract
from PIL import Image
from App.models import Picture
import os


def upload_photo(request):
    # 请求方法为POST时，进行处理
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，则默认为None
        file = request.FILES.get("my_file", None)
        if file is None:
            return JsonResponse(
                {
                    'code': 400,
                    'msg': 'no file'
                }
            )
        else:
            # 打开特定的文件进行二进制的写操作
            with open("./%s" % file.name, 'wb+') as f:
                # 分块写入文件
                for chunk in file.chunks():
                    f.write(chunk)
            # 对图片进行识别
            image = Image.open(file)
            result = pytesseract.image_to_string(image)
            content = []
            for i in result:
                content.append(i)
            # 将识别出的字母，以列表的形式存入数据库
            picture_new = Picture(th_data=content)
            picture_new.save()
            # 删除文件
            path = "./%s" % file.name
            os.remove(path)
            return JsonResponse(
                {
                    'code': 200,
                    'msg': 'success',
                    'content': content,
                }
            )
    else:
        return JsonResponse(
            {
                'code': 400,
                'msg': 'defeat',
            }
        )
