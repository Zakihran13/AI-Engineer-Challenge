# synapsis
### by: MUHAMMAD SUZAKI ZAHRAN


## Preparation
- make sure that this program already installed:
    1. pdm
    2. conda
    3. jupyter notebook (training model only)
    4. postman (testing only)
- training model:
    - the requirements for training is specific for conda env
    - the training model using jupyter notebook
- implementation and integration:
    1. cli: using python PDM
    2. api: docker


## CLI Running
1. install pdm
2. open cli (command-prompt), go to `/SYNAPSIS`
3. run `pdm install` for installing the virtual env
4. if success:
    - run `pdm run python src/synapsis` for listing the menu.
    - run `pdm run python src/synapsis start-db` for initiating database schema on the first run.
    - run `pdm run python src/synapsis start-inferencing` for running the inferencing process.
    - add `--help` at the end of every command will listing all the parameters needed.


## DOCKER Running
1. open cli (command-prompt), go to `/SYNAPSIS`
2. run `docker build -t synapsis-app .` on cli
3. if success, run `docker run -d -p 8000:8000 synapsis-app` to run the local server
4. open postman:
    - add new post request.
    - use `http://0.0.0.0:8000/start_db` for initiating database schema on the first run.
    - use `http://0.0.0.0:8000/start_inferencing` for running the inferencing process. the inferencing needs 3 parameters that input inside json body:
        - `id_karyawan` : id of the worker.
        - `nama_karyawan` : name of the worker.
        - `source_dir` : image dir path, make sure that this image is inside `SYNAPSIS/src/synapsis/model/model training/testing-images` before running the `docker build`.

example of body json for postman:
```
{
    "id_karyawan":"123456789",
    "nama_karyawan":"KYUNGSOO",
    "source_dir":"src/synapsis/model/model training/testing-images/test - single.jpg"
}
```
        