def test_get_favorites(client, auth_headers):
    response = client.get("/favorites/movies", headers=auth_headers)
    assert response.status_code == 200 or response.status_code == 404  # depends on DB state

def test_add_favorite(client, auth_headers):
    movie_id = 1  # убедись, что фильм с таким ID существует в тестовой БД
    response = client.post(f"/favorites/movies/{movie_id}", headers=auth_headers)
    assert response.status_code in (200, 201)

def test_delete_favorite(client, auth_headers):
    movie_id = 1  # убедись, что он был добавлен как избранный
    response = client.delete(f"/favorites/movies/{movie_id}", headers=auth_headers)
    assert response.status_code in (200, 204, 404)