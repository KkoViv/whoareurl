# whoareurl

`whoareurl` is a minimal web fingerprinting tool built for study and CTF practice.

The goal is not to replace tools such as Burp Suite or OWASP ZAP. The goal is to build a small, readable Python program that helps understand how HTTP responses can reveal useful information during a web challenge.

## Project Goal

`whoareurl` analyzes a web target and collects basic fingerprinting data from HTTP responses.

The program is designed to be educational: when an interesting header is found, the tool should explain why that header may matter during reconnaissance.

One important design point is that the tool must inspect every response in a redirection chain, not only the final response.

## Current Scope

The first version is focused on:

- reading user input with `argparse`;
- accepting an IP address or a hostname;
- accepting a port value;
- creating an HTTP request;
- handling HTTP redirects with a custom `HTTPRedirectHandler` used by `urllib.request`;
- storing data extracted from each HTTP response;
- analyzing useful response headers;
- displaying the analyzed data in a readable way.

Hostname validation is intentionally not part of the first implementation because it is more complex than IP and port validation.

## Program Flow

The base program flow is:

```text
1. Parse user input with argparse
2. Store parsed input in a shared data container
3. Create the custom HTTP redirect handler class
4. Run the function that creates the HTTP request and receives responses
5. Store extracted response data as a list of response data sets
6. Run the analysis function on the collected data
7. Display the analysis result
8. End the program with bye_bye
```

## Data Model Idea

The program needs to handle one or more HTTP responses.

This is especially important when the target returns redirects. Since the number of responses is not known in advance, response data is stored as a list of data sets.

Conceptually:

```text
[
    response_1_data,
    response_2_data,
    response_3_data
]
```

Each response data set contains the information extracted from one HTTP response.

## Useful Headers

The first useful headers to inspect are:

- `Server`: declared web server technology.
- `X-Powered-By`: declared application technology.
- `Content-Type`: response body type.
- `Set-Cookie`: session technology and cookie security signals.
- `Location`: redirect target.
- `Content-Length`: declared response body size.
- `Content-Encoding`: compression or encoding behavior.
- `ETag`: cache and resource version behavior.
- `Strict-Transport-Security`: HTTPS enforcement policy.
- `Content-Security-Policy`: browser security policy.
- `X-Content-Type-Options`: content sniffing protection.
- `Referrer-Policy`: referrer leakage control.
- `Permissions-Policy`: browser feature permissions.
- `WWW-Authenticate`: authentication method required by the server.
- `Allow`: HTTP methods allowed by the resource.
- `Via`: proxy or gateway information.
- `Access-Control-Allow-Origin`: CORS exposure behavior.

## Main Components

Planned components:

- `main`: orchestrates the program flow.
- `checkport`: validates the port value passed through `argparse`.
- `SharedData`: stores data shared between program functions.
- `http_redirect_handler`: module for `CustomHttpRedirectHandler`, the custom class used to work with `HTTPRedirectHandler`.
- `redirection`: creates the HTTP request and collects response data.
- `analyze`: analyzes the collected response data.
- `display`: displays analysis results.
- `bye_bye`: closes the program gently.

## Learning Focus

This project is also a Python learning exercise.

The code should stay:

- small;
- readable;
- explicit;
- easy to debug;
- focused on the basic HTTP flow before adding advanced features.

Advanced features should be added only after the basic request, redirect tracking, analysis, and display flow is clear and working.
