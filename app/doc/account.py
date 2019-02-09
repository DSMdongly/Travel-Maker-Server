REGISTER_SPEC = {
    'tags': ['계정'],
    'description': '회원가입 API',
    'parameters': [
        {
            'name': 'id',
            'description': '사용자 ID. 영문, 숫자 포함 20자 이하',
            'in': 'form',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'password',
            'description': '사용자 비밀번호. 영문 숫자 포함 20자 이하',
            'in': 'form',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'name',
            'description': '사용자 닉네임. 영문 숫자 포함 20자 이하',
            'in': 'form',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'phone',
            'description': '사용자 핸드폰 번호',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'email',
            'description': '사용자 이메일 주소',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'join_method',
            'description': '회원가입 방식: 기본값 local, (일반: local, 페북: facebook)',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'social_api_token',
            'description': '소셜 가입시 필요한 토큰',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
    ],
    'responses':  {
        '200': {
            'description': '성공, access_token, refresh_token 발급',
            'examples': {
                'application/json': {
                    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.ey...",
                    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.e...",
                }
            }
        }
    }
}

AUTH_LOCAL_SPEC = {
    'tags': ['계정'],
    'description': '로컬 로그인 API',
    'parameters': [
        {
            'name': 'id',
            'description': '사용자 ID. 영문, 숫자 포함 20자 이하',
            'in': 'form',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'password',
            'description': '사용자 비밀번호. 영문 숫자 포함 20자 이하',
            'in': 'form',
            'type': 'str',
            'required': True,
        },
    ],
    'responses':  {
        '200': {
            'description': '성공, access_token, refresh_token 발급',
            'examples': {
                'application/json': {
                    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.ey...",
                    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.e...",
                }
            }
        }
    }
}


AUTH_SOCIAL_SPEC = {
    'tags': ['계정'],
    'description': '소셜 로그인 API',
    'parameters': [
        {
            'name': 'login_method',
            'description': '로그인 방식: 기본값 facebook, (페북: facebook)',
            'in': 'form',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'social_api_token',
            'description': '소셜 가입시 필요한 토큰',
            'in': 'form',
            'type': 'str',
            'required': True,
        },
    ],
    'responses':  {
        '200': {
            'description': '성공, access_token, refresh_token 발급',
            'examples': {
                'application/json': {
                    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.ey...",
                    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.e...",
                }
            }
        }
    }
}


REFRESH_SPEC = {
    'tags': ['계정'],
    'description': '토큰 재발급 API',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT 인증 헤더 (Authorization: JWT ${refesh_token})',
            'in': 'header',
            'type': 'str',
            'required': True,
        },
    ],
    'responses':  {
        '200': {
            'description': '성공, access_token, 재발급',
            'examples': {
                'application/json': {
                    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.ey...",
                }
            }
        }
    }
}
