import enum

import streamlit as st

from core.state import Metadata
from events.metadata import find_license_index
from events.metadata import handle_metadata_change
from events.metadata import LICENSES
from events.metadata import LICENSES_URL
from events.metadata import MetadataEvent


def render_metadata():
    """Renders the `Metadata` view."""
    metadata = st.session_state[Metadata]
    index = find_license_index(metadata.license)
    key = "metadata-license"
    st.selectbox(
        label="License",
        help=(
            "More information on license names and meaning can be found"
            f" [here]({LICENSES_URL})."
        ),
        key=key,
        options=LICENSES.keys(),
        index=index,
        on_change=handle_metadata_change,
        args=(MetadataEvent.LICENSE, metadata, key),
    )
    key = "metadata-citation"
    st.text_area(
        label="Citation",
        key=key,
        value=metadata.citation,
        placeholder="@book{\n  title={Title}\n}",
        on_change=handle_metadata_change,
        args=(MetadataEvent.CITATION, metadata, key),
    )