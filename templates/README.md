# Minimal STAC Templates

This directory provides minimal STAC 1.0.0 compliant templates to support customer-side creation of STAC entities.

## Purpose

The templates define the smallest valid structures required to create:

* A STAC Collection
* A STAC Item

They are intended as starting points for customer-owned STAC ingestion into a dedicated [endpoint](https://proxy.dev.services.eodc.eu/collections)

## Version

All templates follow the STAC Core specification:

stac_version: "1.0.0"

## Scope

The templates:

* Contain required STAC fields
* Use placeholder values where appropriate
* Are suitable for direct JSON-based ingestion

## Recommended Usage

Users may:

* Edit the JSON templates directly and POST them to the STAC API
* Optionally use libraries such as pystac for programmatic creation and validation

The templates define structure only. Concrete example data is provided separately in the sample_data directory.
