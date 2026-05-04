function normalizeName(name) {
  return (name || "").trim();
}

function greet(name) {
  const normalized = normalizeName(name);
  if (!normalized) {
    return "Hello, friend!";
  }

  return `Hello, ${normalized}!`;
}

module.exports = { greet };
