import React, { useState } from 'react';
import { Container, CssBaseline, Box, Typography, TextField, FormControlLabel, Checkbox, Button, Grid, Link, Avatar } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import { login, getUserId } from '../../Capa_Datos/authService.js'; // Importar las funciones de login y getUserId desde authService.js
import './login.css';

function Login({ onLogin }) {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (event) => {
    event.preventDefault();
    try {
      const loginData = await login(email, password);
      if (loginData.result) {
        const userData = await getUserId(email);
        console.log("User data after getting ID:", userData); // Verifica los datos del usuario con ID
        onLogin(userData.data); // Pasar los datos de login al componente principal
        navigate('/feed'); // Redirigir al feed después de obtener el ID del usuario
      } else {
        setError('Login failed. Please check your credentials.');
      }
    } catch (error) {
      setError('Login failed. Please check your credentials.');
    }
  };

  return (
    <Container component="main" maxWidth="xs" className="login-container">
      <CssBaseline />
      <Box
        className="login-box"
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
          SocialU
        </Typography>
        {error && <Typography color="error">{error}</Typography>}
        <Box component="form" noValidate sx={{ mt: 1 }} onSubmit={handleLogin}>
          <TextField
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email Address"
            name="email"
            autoComplete="email"
            autoFocus
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <FormControlLabel
            control={<Checkbox value="remember" color="primary" />}
            label="Remember me"
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
          >
            Login
          </Button>
          <Grid container>
            <Grid item xs>
              <Link href="#" variant="body2">
                Forgot password?
              </Link>
            </Grid>
            <Grid item>
              <Link href="#" variant="body2" onClick={() => navigate('/register')}>
                {"Don't have an account? Sign Up"}
              </Link>
            </Grid>
          </Grid>
        </Box>
      </Box>
    </Container>
  );
}

export default Login;
