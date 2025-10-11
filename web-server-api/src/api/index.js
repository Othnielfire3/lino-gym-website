const express = require('express');
const router = express.Router();

// Example API endpoint
router.get('/api/example', (req, res) => {
    res.json({ message: 'This is an example API endpoint' });
});

// Add more API endpoints here

module.exports = router;