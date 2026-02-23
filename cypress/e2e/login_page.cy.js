describe("Login Page", () => {
  it("loads successfully", () => {
    cy.visit("/");
    cy.contains("Login");
  });
});
