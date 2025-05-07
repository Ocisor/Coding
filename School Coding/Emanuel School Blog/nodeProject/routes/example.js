const express = require("express")
const router = express.Router()

router.get('/', (req, res) => {
    res.send("Test Page \n ADD ejs file to views")
})


module.exports = router