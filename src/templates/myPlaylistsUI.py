import streamlit as st
import pandas as pd
from view import View
import time

class MyPlaylistsUI:
    @staticmethod
    def main():
        st.header("My playlists")