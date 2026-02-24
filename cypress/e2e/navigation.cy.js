describe("Login Page", () => {
  it("admin navbar", () => {
    cy.admin_login();
    cy.get('[data-testid="dashboard_button"]').should("be.visible");
    cy.get('[data-testid="promote_user_button"]').should("be.visible");
    cy.get('[data-testid="new_ticket_button"]').should("be.visible");
    cy.get('[data-testid="logout_button"]').should("be.visible");
  });

  it("user navbar", () => {
    cy.user_login();
    cy.get('[data-testid="dashboard_button"]').should("be.visible");
    cy.get('[data-testid="promote_user_button"]').should("not.exist");
    cy.get('[data-testid="new_ticket_button"]').should("be.visible");
    cy.get('[data-testid="logout_button"]').should("be.visible");
  });
});
