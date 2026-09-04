# Hosted API Terms of Service

These are the service terms for calling the hosted API at `spacex-api.rone.dev`.
They are separate from the source-code licence in [LICENSE](LICENSE), which
places this project's own code in the public domain under CC0 1.0 and governs
the code rather than the service.

Site-wide terms are at <https://rone.dev/terms>. Where this document is more
specific about the hosted API, it governs.

## Independence and non-affiliation

This project is independent and community-maintained. It is **not** affiliated
with, endorsed by, sponsored by, or operated by Space Exploration Technologies
Corp.

"SpaceX", "Dragon", "Falcon" and all related names, marks and logos belong to
their respective owners. They are used descriptively, to say what the data is
about, and not as an identifier of this project.

The service reads publicly published mission information and re-serves it in a
structured form. The underlying data belongs to its original publisher and all
rights remain with them. **CC0 covers this project's code, not the data it
relays.**

## No warranty

Data is provided as-is, with no warranty of accuracy, completeness, timeliness
or availability.

This matters more here than on most APIs: launch times, windows and vehicle
assignments change frequently and at short notice, and a cached answer can be
wrong within minutes. **Do not use this service for anything operational,
safety-related, or time-critical.** Verify against the official source. The
maintainer accepts no liability for decisions made on the basis of this data.

## No service level

This is a free public endpoint. There is no uptime commitment.

- Endpoints may be rate limited, moved, or withdrawn.
- When the service is shedding load, the data routes are not registered at all
  rather than each view failing individually, so they answer 404 while the root
  endpoint stays up and describes the state. Read the root endpoint rather than
  inferring the state from a single 404.
- Handle failure properly and cache what you can.

## Acceptable use

- Do not send traffic that degrades the service for others. Automated load that
  does may be blocked without notice.
- The root endpoint is a directory of every other endpoint. Read it once instead
  of probing.

## Attribution

Attribution is requested rather than contractually required: a visible credit
linking to <https://spacex-api.rone.dev> wherever you present data from this
service, and a credit to the original publisher of the underlying mission data.

This service does not currently return a machine-readable credit line in its
responses. If attribution should be mandatory, that field goes into the
responses first — asking people to reproduce a line the API never gave them
would be a term nobody could comply with reliably.

## Commercial use

Using the hosted endpoint commercially, beyond what CC0 and this document
already permit, is by arrangement — mostly so we know what load to expect.
Contact us.

## Takedown

If you represent the data source or hold a mark this project touches, and you
want something changed or removed, contact us and it will be actioned. You do
not need a lawyer to make the request and we will not require one to act on it.

We answer within three business days and say what we did.

## Security

Report vulnerabilities to <founder@rone.dev>. Do not open a public issue for a
security problem. Scope and safe-harbour terms are at <https://rone.dev/security>.

## Contact

- Operator: PT RoneAI Teknologi Internasional (RoneAI), Boyolali Regency, Central Java, Indonesia
- Maintainer: ridwaanhall
- General and commercial enquiries: <hello@rone.dev>
- Security: <founder@rone.dev>
- Website: <https://rone.dev>
