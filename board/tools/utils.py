# ip 가져오는 함수
# 사용자의 요청 가져올 때 HttpRequest 객체 사용
# HttpRequest 객체
# HttpRequest.META : headers 정보가 들어 있음
# REMOTE_ADDR : client 의 ip 가져오기
# HTTP_USER_AGNET : client 의 브라우저 정보 가져오기


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[-1].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
