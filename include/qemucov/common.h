
typedef struct qemucov_image_info{
    target_ulong start;
    target_ulong end;
    char * module_path;
    target_ulong module_id;
    struct qemucov_image_info * next;

}qemucov_image_info;


typedef struct qemucov_bb_bitmap {
    target_ulong size;
    target_ulong bitmap_size;
    char * bitmap;
}qemucov_bb_bitmap;


extern qemucov_image_info * qemucov_image_mapping_list;
extern qemucov_bb_bitmap **qemucov_bb_exec_map;
void qemucov_setup(void);
qemucov_bb_bitmap * qemucov_bb_bitmap_alloc(target_ulong seg_size);
void qemucov_bb_bitmap_free(qemucov_bb_bitmap * map);
void qemucov_generate_cov_file(void);