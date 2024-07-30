// src/services/authService.js
const API_URL = 'http://localhost:1002'; // Asegúrate de reemplazar esto con la URL correcta de tu backend

export const login = async (email, password) => {
  const response = await fetch(`${API_URL}/security/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ login_email: email, login_password: password }),
  });

  if (!response.ok) {
    throw new Error('Login failed');
  }

  const data = await response.json();
  return data;
};

export const getUserId = async (email) => {
  const response = await fetch(`${API_URL}/security/user-id?email=${email}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error('Failed to fetch user ID');
  }

  const data = await response.json();
  return data;
};

export const getPosts = async () => {
  const response = await fetch(`${API_URL}/post/list`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error('Failed to fetch posts');
  }

  const data = await response.json();
  console.log('Response data:', data); // Agregar un log para revisar la estructura de la respuesta
  return data[0]?.data || []; // Acceder correctamente a los datos
};

export const createPost = async (usuario_id, contenido) => {
  const response = await fetch(`${API_URL}/post/create`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ usuario_id, contenido }),
  });

  if (!response.ok) {
    throw new Error('Failed to create post');
  }

  const data = await response.json();
  return data;
};

export const registerUser = async (userData) => {
  const response = await fetch(`${API_URL}/user/create`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  });

  if (!response.ok) {
    throw new Error('Failed to register user');
  }

  const data = await response.json();
  return data;
};

export const getFriendRequests = async () => {
  const response = await fetch(`${API_URL}/friendrequest/list`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error('Failed to fetch friend requests');
  }

  const data = await response.json();
  return data;
};

export const createFriendRequest = async (requestData) => {
  const response = await fetch(`${API_URL}/friendrequest/create`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(requestData),
  });

  if (!response.ok) {
    throw new Error('Failed to create friend request');
  }

  const data = await response.json();
  return data;
};

export const updateFriendRequest = async (request_id, status) => {
  const response = await fetch(`${API_URL}/friendrequest/update/${request_id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ status }),
  });

  if (!response.ok) {
    throw new Error('Failed to update friend request');
  }

  const data = await response.json();
  return data;
};

export const deleteFriendRequest = async (request_id) => {
  const response = await fetch(`${API_URL}/friendrequest/delete/${request_id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error('Failed to delete friend request');
  }

  const data = await response.json();
  return data;
};

export const getUsers = async () => {
  const response = await fetch(`${API_URL}/user/list`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error('Failed to fetch users');
  }

  const data = await response.json();
  return data;
};

export const getFriends = async (userId) => {
  const response = await fetch(`${API_URL}/amigos/list`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error('Failed to fetch friends');
  }

  const data = await response.json();
  return data;
};

export const createFriend = async (userId, friendId) => {
  const response = await fetch(`${API_URL}/amigos/create`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ userId, friendId }),
  });

  if (!response.ok) {
    throw new Error('Failed to create friend');
  }

  const data = await response.json();
  return data;
};

export const deleteAmigo = async (amigoId) => {
  const response = await fetch(`${API_URL}/amigos/delete/${amigoId}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error('Failed to delete friend');
  }

  const data = await response.json();
  return data;
};

// *********************SERVICIOS MENSAJES*****************************************************
export const getMessages = async () => {
  const response = await fetch(`${API_URL}/message/list`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error('Failed to fetch messages');
  }

  const data = await response.json();
  return data;
};

export const getMessagesBySenderAndRecipient = async (remitente_id, destinatario_id) => {
  try {
    const response = await fetch(`${API_URL}/message/list/${remitente_id}/${destinatario_id}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch messages');
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching messages:', error);
    throw error;
  }
};

export const createMessage = async (messageData) => {
  const response = await fetch(`${API_URL}/message/create`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(messageData),
  });

  if (!response.ok) {
    throw new Error('Failed to create message');
  }

  const data = await response.json();
  return data;
};

export const deleteMessage = async (messageId) => {
  const response = await fetch(`${API_URL}/message/delete/${messageId}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error('Failed to delete message');
  }

  const data = await response.json();
  return data;
};


//********************************SERVICIOS USUARIOS****************************************************
export const getUserDetails = async (userId) => {
  const response = await fetch(`${API_URL}/user/details/${userId}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error('Failed to fetch user details');
  }

  const data = await response.json();
  return data;
};

export const getUserPosts = async (userId) => {
  const response = await fetch(`${API_URL}/user/posts/${userId}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error('Failed to fetch user posts');
  }

  const data = await response.json();
  return data;
};