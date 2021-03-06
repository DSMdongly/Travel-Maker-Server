CREATE_SPEC = {
    'tags': ['계획'],
    'description': '계획 생성 API',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT 인증 헤더 (Authorization: JWT ${access_token})',
            'in': 'header',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'title',
            'description': '제목',
            'in': 'form',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'description',
            'description': '소개',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'category',
            'description': '''
                카테고리 (0: 기타, 1: 산, 2: 바다, 3: 계곡, 
                         4: 섬, 5: 핫플레이스, 6: 시티투어,
                         7: 랜드마크, 8: 음식)
                ''',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'location',
            'description': '''
                지역 (
                    1: 서울, 2: 부산, 3: 광주, 4: 대전, 
                    5: 울산, 6: 인천, 7: 울산,
                    8: 충청도, 9: 경기도, 10: 경상도
                    11: 강원도, 12: 제주도
                )
                ''',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'schedules',
            'description': '''
                JSON 2중 배열로
                (n - 1) 번째 인덱스에 일정 이름을 저장한다.
                [
                    ['숙소 휴식', '조개구이', '조개구이'],
                    ['숙소 휴식', '조개구이', '조개구이'],
                    ['숙소 휴식', '조개구이', '조개구이'],
                ]
            ''',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'price',
            'description': '여행 경비 (기본값 0원)',
            'in': 'form',
            'type': 'int',
            'required': False,
        },
        {
            'name': 'image',
            'description': '이미지 파일 (360 x 240)',
            'in': 'form',
            'type': 'int',
            'required': False,
        },
    ],
    'responses':  {
        '200': {
            'description': '성공, 제작된 계획 id',
            'examples': {
                'application/json': {
                    "created": {
                        'id': 2,
                        'category': 0,
                        'category_name': '기타',
                        'location': 10,
                        'location_name': '경상도',
                        'title': '김쌤과 함께 떠나는 포항 투어',
                        'description': '포왕 포왕@@',
                        'schdules': "[[\"숙소 휴식\", \"조개구이\", \"조개구이\"],[\"숙소 휴식\", \"조개구이\", \"조개구이\"],[\"숙소 휴식\", \'조개구이\", \"조개구이\"]]",
                        'price': 100000,
                    }
                }
            }
        }
    }
}

THUMBNAIL_SPEC = {
    'tags': ['계획'],
    'description': '계획 썸네일 이미지 조회 API, image src에 해당 api 호출 링크를 불러온다.',
    'parameters': [
        {
            'name': 'plan_id',
            'description': '수정할 계획의 id',
            'in': 'form',
            'type': 'int',
            'required': True,
        },
    ],
    'responses':  {
        '200': {
            'description': '성공, 썸네일 이미지',
        },
        '404': {
            'description': '실패, 이미지가 존재하지 않음',
        },
    }
}

LIST_SPEC = {
    'tags': ['계획'],
    'description': '계획 검색 API',
    'parameters': [
        {
            'name': 'title',
            'description': '제목',
            'in': 'query',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'category',
            'description': '''
                카테고리 (0: 기타, 1: 산, 2: 바다, 3: 계곡, 
                         4: 섬, 5: 핫플레이스, 6: 시티투어,
                         7: 랜드마크, 8: 음식)
                ''',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'location',
            'description': '''
                지역 (
                    1: 서울, 2: 부산, 3: 광주, 4: 대전, 
                    5: 울산, 6: 인천, 7: 울산,
                    8: 충청도, 9: 경기도, 10: 경상도
                    11: 강원도, 12: 제주도
                )
                ''',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'price_range',
            'description': '''
                최대 2개까지 ',' 로 이어붙이기
                여행 경비 가격대 쿼리 n원 대 n원 이상 m원 이하
                'n': n원대
                'n,m': n원 이상 n원 이하
            ''',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
    ],
    'responses':  {
        '200': {
            'description': '성공, plan 목록 조회',
            'examples': {
                'application/json': {
                    "plans": [
                        {
                            'id': 2,
                            'category': 0,
                            'category_name': '기타',
                            'location': 10,
                            'location_name': '경상도',
                            'title': '김쌤과 함께 떠나는 포항 투어',
                            'description': '포왕 포왕@@',
                            'schdules': "[[\"숙소 휴식\", \"조개구이\", \"조개구이\"],[\"숙소 휴식\", \"조개구이\", \"조개구이\"],[\"숙소 휴식\", \'조개구이\", \"조개구이\"]]",
                            'price': 100000,
                        }
                    ]
                }
            }
        }
    }
}


UPDATE_SPEC = {
    'tags': ['계획'],
    'description': '계획 수정 API',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT 인증 헤더 (Authorization: JWT ${access_token})',
            'in': 'header',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'plan_id',
            'description': '수정할 계획의 id',
            'in': 'form',
            'type': 'int',
            'required': True,
        },
        {
            'name': 'title',
            'description': '제목',
            'in': 'form',
            'type': 'str',
            'required': True,
        },
        {
            'name': 'description',
            'description': '소개',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'category',
            'description': '''
                카테고리 (0: 기타, 1: 산, 2: 바다, 3: 계곡, 
                         4: 섬, 5: 핫플레이스, 6: 시티투어,
                         7: 랜드마크, 8: 음식)
                ''',
            'in': 'form',
            'type': 'int',
            'required': False,
        },
        {
            'name': 'location',
            'description': '''
                지역 (
                    1: 서울, 2: 부산, 3: 광주, 4: 대전, 
                    5: 울산, 6: 인천, 7: 울산,
                    8: 충청도, 9: 경기도, 10: 경상도
                    11: 강원도, 12: 제주도
                )
                ''',
            'in': 'form',
            'type': 'int',
            'required': False,
        },
        {
            'name': 'schedules',
            'description': '''
                JSON 2중 배열로
                (n - 1) 번째 인덱스에 일정 이름을 저장한다.
                [
                    ['숙소 휴식', '조개구이', '조개구이']
                    ['숙소 휴식', '조개구이', '조개구이']
                    ['숙소 휴식', '조개구이', '조개구이']
                ]
            ''',
            'in': 'form',
            'type': 'str',
            'required': False,
        },
        {
            'name': 'price',
            'description': '여행 경비 (기본값 0원)',
            'in': 'form',
            'type': 'int',
            'required': False,
        },
        {
            'name': 'image',
            'description': '이미지 파일 (360 x 240)',
            'in': 'form',
            'type': 'int',
            'required': False,
        },
    ],
    'responses':  {
        '200': {
            'description': '성공, 업데이트 된 게획의 id',
            'examples': {
                'application/json': {
                    "updated": {
                        'id': 2,
                        'category': 0,
                        'category_name': '기타',
                        'location': 10,
                        'location_name': '경상도',
                        'title': '김쌤과 함께 떠나는 포항 투어~~',
                        'description': '포왕 포왕@@',
                        'schdules': "[[\"숙소 휴식\", \"조개구이\", \"조개구이\"],[\"숙소 휴식\", \"조개구이\", \"조개구이\"],[\"숙소 휴식\", \'조개구이\", \"조개구이\"]]",
                        'price': 100000,
                    }
                }
            }
        }
    }
}


DELETE_SPEC = {
    'tags': ['계획'],
    'description': '계획 삭제 API',
    'parameters': [
        {
            'name': 'plan_id',
            'description': '수정할 계획의 id',
            'in': 'form',
            'type': 'int',
            'required': True,
        },
    ],
    'responses':  {
        '200': {
            'description': '성공, 삭제된 게획의 id',
            'examples': {
                'application/json': {
                    "deleted": {
                        'id': 2,
                    }
                }
            }
        }
    }
}