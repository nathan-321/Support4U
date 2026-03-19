describe("Register Page", { testIsolation: true }, () => {
  it("Can't create an account with short password", () => {
    cy.visit("/", { failOnStatusCode: false });
    cy.get('[data-testid="register_button"]').should("be.visible").click();
    cy.get('[data-testid="register_username_input"]').click().type("Amy");
    cy.get('[data-testid="register_email_input"]')
      .click()
      .type("amy@email.com");
    cy.get('[data-testid="register_password_input"]').click().type("123");
    cy.get('[data-testid="register_submit_button"]').click();
    cy.contains("Your password doesn't meet the requirements!").should(
      "be.visible"
    );
  });
});
