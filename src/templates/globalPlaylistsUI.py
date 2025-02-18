import streamlit as st
import pandas as pd
from view import View
import time

class GlobalPlaylistsUI:
    @staticmethod
    def main():
        st.header("Manage Global Playlists")