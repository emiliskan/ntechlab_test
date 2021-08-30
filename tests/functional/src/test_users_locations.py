import pytest
import pytest_cases

API_URL = 'users/location'


@pytest_cases.parametrize(
    "user_id, radius, count, answer",
    [
        (1, 1, 2, []),
        (1, 2, 5, []),
        (1, 100, 5, []),
        (2, 100, 5, []),
        (3, 1, 5, []),
    ],
)
@pytest.mark.asyncio
async def test_near_users(make_get_request, user_id, radius, count):

    url = f"{API_URL}/near?user_id={user_id}&radius={radius}&count={count}"
    response = await make_get_request(
        method=url,
    )
    assert response.status == 400
