client ID : 우리가 만들고 있는 어플리케이션을 식별하는 식별자(외부에 노출되어도 괜찮음)
client Secret : 식별자에 대한 비밀번호(외부에 노출되면 절대 안 됨)
authorized redirect URLs : 리소스 서버가 권한을 부여하는 과정에서 우리에게 authorized 코드를 전달해주는데, 그때 이 주소로 전달해달라고 함. 리소스 서버는 다른 주소에서 요청하면 무시함

리소스 서버가 클라이언트들에게 우리를 쓰려면 이렇게 해야 한다고 방식을 알려줌. 그 방식이 API(Application Programming Interface)

refresh token : 액세스 토큰의 유효 기간이 다 되었을 때, 액세스 토큰을 간단하게 다시 받을 수 있게 해주는 토큰