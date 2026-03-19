describe("Testing RBAC", { testIsolation: false }, () => {
  before(() => {
    cy.user_login();
  });

  it("Normal User unable to view promote a user button in navbar", () => {
    cy.get('[data-testid="promote_user_button"]').should("not.exist");
  });

  it("Normal User unable to promote a user via route", () => {
    cy.visit("/promote-user/9", { failOnStatusCode: false });
    cy.contains(
      "You don't have the permission to access the requested resource"
    ).should("be.visible");
  });

  it("Normal User unable to delete a user via route", () => {
    cy.visit("/delete-ticket/9", { failOnStatusCode: false });
    cy.contains(
      "You don't have the permission to access the requested resource"
    ).should("be.visible");
  });
});
