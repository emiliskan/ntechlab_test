import pytest
import pytest_cases

API_URL = 'users/'


@pytest_cases.parametrize(
    "user_id, name, x, y",
    [
        (15, "Alex", 100, 210),
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
    assert response.status == 200


@pytest_cases.parametrize(
    "user_id, name, x, y",
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


@pytest_cases.parametrize(
    "user_id, name, x, y",
    [
        (15, "Alex", 100, 210),
    ],
)
@pytest.mark.asyncio
async def test_save_user(make_put_request, user_id, name, x, y):
    response = await make_put_request(
        method=f"{API_URL}/",
        data={
            "id": user_id,
            "x": x,
            "y": y,
            "name": name
        }
    )
    assert response.status == 200
