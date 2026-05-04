const test = require("node:test");
const assert = require("node:assert/strict");
const { greet } = require("./greetings");

test("greet returns a greeting with name", () => {
  assert.equal(greet("Totor"), "Hello, Totor!");
});

test("greet returns default greeting for empty input", () => {
  assert.equal(greet(""), "Hello, friend!");
  assert.equal(greet("   "), "Hello, friend!");
});
