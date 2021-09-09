from os import listdir, remove
from os.path import exists, isdir


EDGE = "C:/Program Files (x86)/Microsoft/Edge/Application/"
FILES = ["ie_to_edge_bho.dll", "ie_to_edge_bho_64.dll", "ie_to_edge_stub.exe"]
INFO = (
    "Author: Forest Jacobsen (https://github.com/ForestJ2)\n"
    """
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
)


def main():
    dirs = []

    if exists(EDGE) is False or isdir(EDGE) is False:
        print(f"[ERROR] folder '{EDGE}' could not be found")
        return

    print(f"[INFO] found Edge at '{EDGE}'")
    dirs = [item for item in listdir(EDGE) if isdir(EDGE + item)]

    for directory in dirs:
        full_path = EDGE + directory + "/BHO/"

        if exists(full_path):
            print(f"[INFO] found path '{full_path}'")
            remove_bad_software(full_path)

    input("\nPress Enter to exit...")


def remove_bad_software(directory):
    for f in FILES:
        file_path = directory + f

        try:
            if exists(file_path):
                remove(file_path)

            print(f"[INFO] deleted file '{file_path}'")

        except Exception as e:
            print(f"[ERROR] could not delete '{file_path}', it may not exist")
            print(f"[DEBUG] {e}")


if __name__ == "__main__":
    print(INFO)
    main()
