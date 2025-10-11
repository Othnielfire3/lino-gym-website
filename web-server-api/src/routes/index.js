import express from 'express';
import apiRoutes from '../api/index.js';

const router = express.Router();

const setupRoutes = (app) => {
    app.use('/api', apiRoutes);
};

export default setupRoutes;