from data.components.footer_data import COPYRIGHT_TEXT

def test_check_footer_is_visible_and_has_right_text(auth_inventory_page):
    assert auth_inventory_page.footer.get_copyright_text() == COPYRIGHT_TEXT