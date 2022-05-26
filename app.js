const express = require("express")
const ejs = require("ejs") //View engine
var app = express()
const path = require("path")

//Setting view engine
app.set("view engine", "ejs")

app.use(express.static(path.join(__dirname, "/public")))
console.log(__dirname + "/public")

//--------------ROUTES-----------------------

//GET request to homepage
app.get("/", (req, res) => {
  res.render("index")
})

app.get("/search", function (req, res) {
  console.log("Running")
  const query = req.query
  const question = query.question
  // Use child_process.spawn method from
  // child_process module and assign it
  // to variable spawn

  if (question != "") {
    var spawn = require("child_process").spawn
    // Parameters passed in spawn -
    // 1. type_of_script
    // 2. list containing Path of the script
    //    and arguments for the script
    console.log("The query is ", question)
    var process = spawn("python", [__dirname + "/query_handling.py", question])

    // Takes stdout data from script which executed
    // with arguments and send this data to res object
    process.stdout.on("data", function (data) {
      console.log("Sending Info")
      // mystr = data.toString("utf8")

      myjson = JSON.parse(data)
      res.json(myjson)
    })
  }
})

//--------------- LISTEN ----------------
//state the port
const PORT = process.env.PORT || 3000
// Creates a server which runs on port 3000 and
// can be accessed through localhost:3000
app.listen(PORT, function () {
  console.log("server running on port 3000")
})
