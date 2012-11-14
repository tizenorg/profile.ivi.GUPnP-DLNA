
#ifndef __gupnp_dlna_marshal_MARSHAL_H__
#define __gupnp_dlna_marshal_MARSHAL_H__

#include	<glib-object.h>

G_BEGIN_DECLS

/* BOOLEAN:STRING,UINT,STRING,POINTER (./gupnp-dlna-marshal.list:1) */
extern void gupnp_dlna_marshal_BOOLEAN__STRING_UINT_STRING_POINTER (GClosure     *closure,
                                                                    GValue       *return_value,
                                                                    guint         n_param_values,
                                                                    const GValue *param_values,
                                                                    gpointer      invocation_hint,
                                                                    gpointer      marshal_data);

/* VOID:OBJECT,BOXED (./gupnp-dlna-marshal.list:2) */
extern void gupnp_dlna_marshal_VOID__OBJECT_BOXED (GClosure     *closure,
                                                   GValue       *return_value,
                                                   guint         n_param_values,
                                                   const GValue *param_values,
                                                   gpointer      invocation_hint,
                                                   gpointer      marshal_data);

G_END_DECLS

#endif /* __gupnp_dlna_marshal_MARSHAL_H__ */

