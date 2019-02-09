PROFILE_SHOW_SPEC = {
    'tags': ['사용자'],
    'description': '프로필 조회 API',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT 인증 헤더 (Authorization: JWT ${access_token})',
            'in': 'header',
            'type': 'str',
            'required': True,
        },
    ],
    'responses':  {
        '200': {
            'description': '성공, access_token, refresh_token 발급',
            'examples': {
                'application/json': {
                    "profile": {
                        "id": "gdh0608",
                        "descritpion": "버블이에요",
                        "email": "gdh0608@naver.com",
                        "keywords": "[\"\\\"버블\\\"\", \"\\\"비눗방울\\\"\"]",
                        "name": "bubble",
                        "phone": "01050554752"
                    }
                }
            }
        }
    }
}


PROFILE_UPDATE_SPEC = {
    'tags': ['사용자'],
    'description': '프로필 수정 API',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT 인증 헤더 (Authorization: JWT ${access_token})',
            'in': 'header',
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
            'name': 'description',
            'description': '사용자 한줄 소개',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'keywords',
            'description': '''
                사용자 키워드(해시태그) 모음 JSON 배열
                "[\"안녕\", \"안녕하세요\", \"맛집투어\"]"
            ''',
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
                    "updated": {
                        "id": "gdh0608",
                        "descritpion": "버블이에요",
                        "email": "gdh0608@naver.com",
                        "keywords": "[\"\\\"버블\\\"\", \"\\\"비눗방울\\\"\"]",
                        "name": "bubble",
                        "phone": "01050554752"
                    }
                }
            }
        }
    }
}


