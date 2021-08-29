import pytest
import pytest_cases

API_URL = 'users/'


@pytest_cases.parametrize(
    "user_id, name", "x", "y",
    [
        (1, "Alex", 1, 2),
        (2, "Sergey", 1, 5),
        (3, "Andrew", 1, 6),
        (4, "John", 2, 42),
    ],
)
@pytest.mark.asyncio
async def test_new_user(make_post_request, user_id, name, x, y):

    response = await make_post_request(
        method=f"{API_URL}/",
        data={
            "id": user_id,
            "x": x,
            "y": y,
            "name": name
        }
    )
    assert response.status == 201, "Couldn't crate users."


@pytest_cases.parametrize(
    "user_id, name", "x", "y",
    [
        (1, "Alex", 1, 2),
    ],
)
@pytest.mark.asyncio
async def test_new_user_exist_error(make_post_request, user_id, name, x, y):

    response = await make_post_request(
        method=f"{API_URL}/",
        data={
            "id": user_id,
            "x": x,
            "y": y,
            "name": name
        }
    )
    assert response.status == 400
