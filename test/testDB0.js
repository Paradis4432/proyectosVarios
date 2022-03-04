const db = require('better-sqlite3')('data.db');
const fs = require('fs');

db.prepare("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)").run();

//db.prepare("INSERT INTO test (name, age) VALUES (@name, @age)").run({name: 'John', age: 42});
//db.prepare("INSERT INTO test (name, age) VALUES (@name, @age)").run({name: 'gap puto', age: 12});

//db.prepare("DELETE FROM test WHERE id = @id").run({id: 1});

//db.prepare("UPDATE test SET name = @name, age = @age WHERE id = @id").run({id: 5, name: 'lucas', age: 25});

db.prepare("SELECT * FROM test").all().forEach(row => {
  console.log(row.id, row.name, row.age);
});
