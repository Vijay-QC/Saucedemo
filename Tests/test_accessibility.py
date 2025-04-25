import requests
import json

def inject_axe_and_run(page):
    # Load axe-core script from CDN
    axe_script = requests.get("https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.8.0/axe.min.js").text
    page.evaluate(axe_script)

    # Run axe on the page
    results = page.evaluate("async () => await axe.run()")
    return results

def test_inventory_accessibility(browser_page):
    results = inject_axe_and_run(browser_page)
    violations = results["violations"]

    for v in violations:
        print(f"Accessibility violation: {v['id']} - {v['description']}")
        for node in v["nodes"]:
            print(f"  Affected element: {node['html']}")

    assert len(violations) == 0, f"{len(violations)} accessibility issues found"
