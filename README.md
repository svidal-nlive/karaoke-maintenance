# karaoke-maintenance

Utility, maintenance, and cookie-exporter microservices for the Karaoke stack.

## Services

- **maintenance**: Handles periodic log cleanup and other admin tasks
- **cookies_exporter**: Exports updated cookies for use by the Telegram bot and other services
- **volume-init**: Optionally used for one-time volume setup

## Usage

1. Clone this repo
2. Copy `.env.example` to `.env` and edit as needed
3. Ensure all required external Docker volumes/networks exist:

    ```bash
    docker volume create logs
    docker volume create cookies
    docker volume create playwright_profile
    docker volume create input
    docker volume create queue
    docker volume create metadata
    docker volume create output
    docker volume create organized
    docker volume create stems
    docker network create backend
    ```

4. Start the maintenance stack:

    ```bash
    docker compose up -d
    ```

5. This project requires the shared library karaoke-shared.
   Install via pip:

    ```
    python -m pip install karaoke-shared
    ```

   Or, for the latest development version:

    ```
    python -m pip install git+https://github.com/svidal-nlive/karaoke-shared.git@main
    ```

   The included requirements.txt installs the latest tagged development version by default.

## Notes

- All volumes and networks must match those used by the main pipeline for full integration.
- Maintenance stack can be run independently for volume prep and log management.
