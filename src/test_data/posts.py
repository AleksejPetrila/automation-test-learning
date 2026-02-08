def new_post_payload(user_id: int = 1, title: str = "Hello", body: str = "Body text") -> dict:
    return {
        "userId": user_id,
        "title": title,
        "body": body,
    }


def put_post_payload(post_id: int = 1, user_id: int = 1,
                     title: str = "Updated title", body: str = "Updated body") -> dict:
    return {
        "id": post_id,
        "userId": user_id,
        "title": title,
        "body": body,
    }
