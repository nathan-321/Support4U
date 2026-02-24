describe("Login Page", { testIsolation: false }, () => {
  it("logins in successfully", () => {
    cy.admin_login();
  });
  it("logs out successfully", () => {
    cy.get('[data-testid="logout_button"]').click();
  });
});
