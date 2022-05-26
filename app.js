const express = require("express")
const ejs = require("ejs") //View engine
var app = express()
const path = require("path")

//Setting view engine
app.set("view engine", "ejs")

app.use(express.static(path.join(__dirname, "/public")))
console.log(__dirname + "/public")

app.use(express.json())

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
    var py = spawn("python", [__dirname + "/query_handling.py", question])
    console.log(__dirname + "/query_handling.py")

    console.log("spawned")

    let output = ""
    // Takes stdout data from script which executed
    // with arguments and send this data to res object
    py.stdout.on("data", function (data) {
      output += data.toString()
      console.log(data.toString())
    })

    py.stderr.on("data", function (data) {
      output += data.toString()
      console.log(data.toString())
    })

    py.on("close", function (exitCode) {
      output = output.trim().match(/[{].*.[}]/) //extract actual content from garbage e.g. JSON between [] or {}
      let result = JSON.parse(output)
      res.json(result)
    })
    // try {
    //   py.stdout.on("data", function (data) {
    //     console.log("Sending Info")
    //     mystr = data.toString("utf8")

    //     myjson = JSON.parse(data)
    //     res.json(myjson)
    //   })
    // } catch (error) {
    //   console.log("Error parsing json", error, data)
    // }
    // py.stdout.on("data", function (data) {
    //   console.log("Sending Info")
    //   mystr = data.toString("utf8")

    //   myjson = JSON.parse(data)
    //   res.json(myjson)
    // })
  }
})

//--------------- LISTEN ----------------
//state the port
const PORT = process.env.PORT || 3000
// Creates a server which runs on port 3000 and
// can be accessed through localhost:3000
app.listen(PORT, function () {
  console.log(`server running on PORT ${PORT}`)
})
