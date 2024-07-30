import React, { useState } from 'react';
import { Container, CssBaseline, Box, Typography, TextField, Button, Grid, Link, Avatar } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import './CrearUsuario.css';
import { registerUser } from '../../Capa_Datos/authService'; // Importa el servicio de registro de usuario

function CrearUsuario() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    nombre: '',
    correo_electronico: '',
    contraseña: '',
    foto_perfil: '',
    fecha_nacimiento: '',
    biografia: ''
  });
  const [profileImage, setProfileImage] = useState(null);
  const [profileImageUrl, setProfileImageUrl] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleImageChange = async (event) => {
    const file = event.target.files[0];
    if (file) {
      const base64 = await convertToBase64(file);
      setFormData({
        ...formData,
        foto_perfil: base64
      });
      setProfileImageUrl(URL.createObjectURL(file));
    }
  };

  const convertToBase64 = (file) => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result);
      reader.onerror = (error) => reject(error);
    });
  };

  const handleRegister = async (event) => {
    event.preventDefault();
    try {
      await registerUser(formData); // Llama al servicio de registro de usuario
      alert("User registered successfully!");
      navigate('/'); // Redirigir a la página de login después del registro
    } catch (error) {
      console.error("Failed to register user:", error);
      alert("Failed to register user.");
    }
  };

  return (
    <Container component="main" maxWidth="xs" className="register-container">
      <CssBaseline />
      <Box
        className="register-box"
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign Up
        </Typography>
        <Box component="form" noValidate sx={{ mt: 1 }} onSubmit={handleRegister}>
          <TextField
            margin="normal"
            required
            fullWidth
            id="nombre"
            label="Nombre"
            name="nombre"
            autoComplete="nombre"
            autoFocus
            value={formData.nombre}
            onChange={handleChange}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            id="correo_electronico"
            label="Correo Electrónico"
            name="correo_electronico"
            autoComplete="email"
            value={formData.correo_electronico}
            onChange={handleChange}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="contraseña"
            label="Contraseña"
            type="password"
            id="contrasena"
            autoComplete="current-password"
            value={formData.contrasena}
            onChange={handleChange}
          />
          <TextField
            margin="normal"
            fullWidth
            id="fecha_nacimiento"
            label="Fecha de Nacimiento"
            type="date"
            name="fecha_nacimiento"
            InputLabelProps={{
              shrink: true,
            }}
            value={formData.fecha_nacimiento}
            onChange={handleChange}
          />
          <TextField
            margin="normal"
            fullWidth
            id="biografia"
            label="Biografía"
            name="biografia"
            autoComplete="biografia"
            multiline
            rows={4}
            value={formData.biografia}
            onChange={handleChange}
          />
          <input
            accept="image/*"
            style={{ display: 'none' }}
            id="foto_perfil"
            type="file"
            onChange={handleImageChange}
          />
          <label htmlFor="foto_perfil">
            <Button variant="contained" component="span" fullWidth sx={{ mt: 2, mb: 2 }}>
              Upload Profile Picture
            </Button>
          </label>
          {profileImageUrl && (
            <Box
              component="img"
              sx={{
                height: 200,
                width: 200,
                maxHeight: { xs: 200, md: 200 },
                maxWidth: { xs: 200, md: 200 },
                borderRadius: '50%',
                mt: 2
              }}
              alt="Profile Preview"
              src={profileImageUrl}
            />
          )}
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
          >
            Sign Up
          </Button>
          <Grid container>
            <Grid item>
              <Link href="#" variant="body2" onClick={() => navigate('/')}>
                {"Already have an account? Login"}
              </Link>
            </Grid>
          </Grid>
        </Box>
      </Box>
    </Container>
  );
}

export default CrearUsuario;
