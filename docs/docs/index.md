# Seli
<p align="center">
  <img  src="https://github.com/yemaney/seli/actions/workflows/test.yaml/badge.svg" alt="Test">
  <img  src="images/coverage.svg" alt="Coverage">
</p>
<h1 align="center">
    configurable selenium workers
</h1>

---

## Workflow

```mermaid
flowchart LR
  1(jobs.json) --> 3;
  2(credentials.json) --> 4;
  3(job reader) --> 5;
  4(credential loader) --> 6;
  5(job) --> 7;
  6(credentials) --> 7;
  7(workers) --> 8(do work)
```

---

## Jobs JSON Schema

```json
{
    "jobs": [workers...]
}

```


!!! info "workers"

    === "browser"
        Used to search a url using the address bar.

        ``` json
        {
            "kind": "browser",
            "url": "https://www.youtube.com/"
        }
        ```

    === "button"
        Used to click a button.

        ``` json
        {
            "kind" : "button",
            "xpath" : "//*[@id='buttons']/ytd-button-renderer"
        }
        ```

    === "field"
        Used to click a button.

        ``` json
        {
            "kind" : "field",
            "xpath" : "//*[@id='identifierId']",
            "text" : "username"
        }
        ```
