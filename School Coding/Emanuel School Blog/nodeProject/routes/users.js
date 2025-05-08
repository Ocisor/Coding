const express = require("express")
const router = express.Router()

router.get('/', (req, res) => {
    res.send("User Page")
})
router.post('/login', (req, res) => {
    
})

module.exports = router