"""Streamlit session state.

In the future, this could be the serialization format between front and back.
"""

import dataclasses

import streamlit as st

import mlcroissant as mlc


def init_state():

    if CurrentStep not in st.session_state:
        st.session_state[CurrentStep] = "start"

    if Files not in st.session_state:
        st.session_state[Files] = []

    if Metadata not in st.session_state:
        st.session_state[Metadata] = Metadata()

    if RecordSets not in st.session_state:
        st.session_state[RecordSets] = []


class CurrentStep:
    start = "start"
    load = "load"
    editor = "editor"


class Files:
    pass


class RecordSets:
    pass


class RecordSet:
    pass


@dataclasses.dataclass
class Metadata:
    name: str = ""
    description: str | None = None
    citation: str | None = None
    license: str | None = ""
    url: str = ""

    def __bool__(self):
        return self.name != "" and self.url != ""
