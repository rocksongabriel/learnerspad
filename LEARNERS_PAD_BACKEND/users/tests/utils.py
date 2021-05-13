def get_user_data(generated_data):
    return {
        "username": generated_data.username,
        "email": generated_data.email,
        "first_name": generated_data.first_name,
        "last_name": generated_data.last_name,
        "password": generated_data.password
    }